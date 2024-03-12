import numpy as np

from .common import Jacobian, NumericalJacobian, UserDefinedJacobian, EPS
from numba import njit
from abc import ABC, abstractmethod
from .interface import Interface
from .common import select_initial_step
from scipy.linalg import lu_solve as lu_solve_scipy, lu_factor as lu_factor_scipy
from .linalg.lapack.lapack_python import lu_factor, lu_solve


def _njit(jit=True):
    def wrapper(fun):
        if jit:
            return njit(fun)
        else:
            return fun
    return wrapper


class BaseMethod(ABC):
    """
    The base method for which the solver methods are derived

    :param interface: The solver-model interface.
    :type interface: :class:`solver.interface.Interface`
    :param use_jit: To use numba jitting of the solver method(s)
    :type use_jit: bool
    :param options: a list of options to pass the solver method(s)
    """
    def __init__(self, interface: Interface, use_jit: bool, **options):
        self.use_jit = use_jit
        self.interface = interface

    @abstractmethod
    def get_solver_state(self):
        """Get the solver state

        :return: tuple of solver method states, passed inside the solver loop. Used to save states for numba.
        :rtype: tuple
        """
        return ()

    @staticmethod
    def step_func(interface: Interface, t: float, dt: float, y: list, yold: list, order: int, _solve_state: tuple):
        """The step method which is executed inside the solver loop.
        """
        raise NotImplementedError


class RK45(BaseMethod):
    """Implementation of the jitable Runga-Kutta 4.5 method. The method is partially copied from \
    :class:`scipy.integrate.RK45`, but has been modified to allow jitting.
    """
    def __init__(self, interface: Interface, use_jit: bool, **options):
        super(RK45, self).__init__(interface, use_jit, **options)
        __njit = _njit(self.use_jit)

        submethod=options['submethod']

        if submethod == None:
            submethod = 'RKDP45'

        if submethod == 'RKF45':

            c = np.zeros(6)
            c[0] = 0
            c[1] = 1 / 4
            c[2] = 3 / 8
            c[3] = 12 / 13
            c[4] = 1
            c[5] = 1 / 2
            a = np.zeros((6, 5))
            b = np.zeros((2, 6))
            a[1, 0] = 1 / 4
            a[2, 0] = 3 / 32
            a[2, 1] = 9 / 32
            a[3, 0] = 1932 / 2197
            a[3, 1] = -7200 / 2197
            a[3, 2] = 7296 / 2197
            a[4, 0] = 439 / 216
            a[4, 1] = -8
            a[4, 2] = 3680 / 513
            a[4, 3] = -845 / 4104
            a[5, 0] = -8 / 27
            a[5, 1] = 2
            a[5, 2] = -3544 / 2565
            a[5, 3] = 1859 / 4104
            a[5, 4] = -11 / 40

            b[1, 0] = 16 / 135
            b[1, 1] = 0
            b[1, 2] = 6656 / 12825
            b[1, 3] = 28561 / 56430
            b[1, 4] = -9 / 50
            b[1, 5] = 2 / 55

            b[0, 0] = 25 / 216
            b[0, 1] = 0
            b[0, 2] = 1408 / 2565
            b[0, 3] = 2197 / 4104
            b[0, 4] = -1 / 5
            b[0, 5] = 0
            self.order = 4
            self.rk_steps = 5
            self.e_order = 5
        elif submethod == 'RKDP45':
            c=np.zeros(7)
            c[0] = 0
            c[1] = 1/5
            c[2] = 3/10
            c[3] = 4/5
            c[4] = 8/9
            c[5] = 1
            c[6] = 1

            a = np.zeros((6,6))
            a[1:] = [1/5, 0, 0, 0, 0 ,0]
            a[2:] = [3/40, 9/40, 0, 0, 0, 0]
            a[3:] = [44/45, -56/15, 32/9, 0, 0, 0]
            a[4:] = [19372/6561, -25360/2187, 64448/6561, -212/729, 0, 0]
            a[5:] = [9017/3168, -355/33, 46732/5247, 49/176, -5103/18656, 0]

            b = np.zeros((2,7))
            b[0:] = [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0]
            b[1:] = [5179/57600, 0, 7571/16695, 393/640, -92097/339200, 187/2100, 1/40]
            self.e_order = 4
            self.order = 5
            self.rk_steps = 5

        else:
            raise Exception("incorrect submethod specified")
        self.y0 = interface.get_states()
        self.f0 = interface.get_deriv(0, self.y0)
        self.a = a
        self.b = b
        self.c = c

        self.error_exponent = (-1 / (self.e_order + 1))
        self.max_factor = options.get('max_factor', 10)
        self.atol = options.get('atol', 1e-3)
        self.rtol = options.get('rtol', 1e-3)

        self.initial_step = select_initial_step(self.interface, 0, self.y0, 1, self.order - 1, self.rtol,
                                                self.atol)

        @__njit
        def Rk45(interface, t, dt, y, _not_used1, _not_used2, _solve_state):

            c = _solve_state[0]
            a = _solve_state[1]
            b = _solve_state[2]
            max_factor = _solve_state[3]
            atol = _solve_state[4]
            rtol = _solve_state[5]
            f0 = _solve_state[6]
            rk_steps = _solve_state[7]
            order = _solve_state[8]
            error_exponent = _solve_state[9]
            last_step = _solve_state[10]
            step_info = 1

            converged = False

            tnew = t+dt

            k = np.zeros((rk_steps+2, len(y)))
            k[0,:] = f0*dt

            for i in range(1,rk_steps+1):
                dy = np.dot(k[:i].T, a[i,:i])
                interface.set_states(y + dy)
                k[i, :] = dt * interface.get_deriv(t + c[i] * dt, y + dy)

            ynew = y + np.dot(k[0:order+2].T, b[0,:])
            interface.set_states(ynew)
            fnew = interface.get_deriv(tnew, ynew)
            k[-1, :] = dt*fnew

            ye = y + np.dot(k[0:order+2].T, b[1,:])
            scale = atol + np.maximum(np.abs(y), np.abs(ynew)) * rtol

            e = (ynew-ye)

            e_norm = np.linalg.norm(e/scale)/ (len(e)**0.5)

            if e_norm < 1:
                if e_norm == 0:
                    factor = max_factor
                else:
                    factor = min(max_factor,
                                 0.95 * e_norm ** error_exponent)

                if not last_step:
                    factor = min(1, factor)

                f0=fnew
                converged = True
            else:
                factor = max(0.2,
                             0.95 * e_norm ** error_exponent)

            _new_solve_state = (c, a, b, max_factor, atol, rtol, np.ascontiguousarray(f0), rk_steps, order,
                                error_exponent, converged)

            return tnew, ynew, converged, step_info, _new_solve_state, factor

        self.step_func = Rk45

    def get_solver_state(self):
        return (self.c, self.a, self.b, self.max_factor, self.atol, self.rtol, self.f0, self.rk_steps, self.order,
                self.error_exponent, True)


class BDF(BaseMethod):
    """Implementation of the jitable BDF method for numba. [2]_. The method is partially copied from \
    :class:`scipy.integrate.BDF`, but has been modified to allow jitting.

    References
    ----------
    .. [2] L.F. Shampine, M.W. Reichelt, "The MATLAB ODE Suite", SIAM Journal on Scientic Computing, 1997, Vol 18, \
            Issue 1

    """

    def __init__(self, interface: Interface, use_jit: bool, **options):
        super(BDF, self).__init__(interface, use_jit, **options)

        __njit = _njit(self.use_jit)

        max_order = 5
        self.order = max_order

        # Get options
        inner_itermax = options.get('inner_itermax', 4)
        abs_tol = options.get('atol', 0.001)
        rel_tol = options.get('rtol', 0.001)
        shorter = options.get('shorter', 0.8)

        self.y0 = interface.get_states()
        self.abs_tol = abs_tol

        try:
            self.interface.get_jacobian(0)
            jac: UserDefinedJacobian = UserDefinedJacobian(interface=self.interface)
            self.J = jac.get_jacobian(0)

        except NotImplementedError:
            jac: NumericalJacobian = NumericalJacobian(interface=self.interface, tolerance=abs_tol)
            self.J = jac.get_jacobian(0)
        self.jac = jac
        self.initial_step = select_initial_step(self.interface, 0, self.y0,
                                                           1, 1, rel_tol,
                                                           abs_tol)

        newton_tol = max(10 * EPS / rel_tol, min(0.03, rel_tol ** 0.5))

        @__njit
        def update_D(I, J, U, D, order, factor):
            I_ = I[order-1]
            J_ = J[order-1]
            U_ = U[order-1]
            R = calculate_R(I_, J_, order, factor)
            #U = calculate_R(I_, J_, order, 1)
            RU = R.dot(U_)
            D[:order + 1] = np.dot(RU.T, D[:order + 1])
            return D

        @__njit
        def calculate_R(I, J, order, factor):
            """Compute the matrix for changing the differences array."""
            M = np.zeros((order + 1, order + 1))
            M[1:, 1:] = (I - 1 - factor * J) / I
            M[0] = 1
            R = np.empty_like(M)
            for i in range(order + 1):
                R[:, i] = np.cumprod(M[:, i])
            return R

        gamma = np.hstack((0, np.cumsum(1 / np.arange(1, max_order + 1))))
        kappa = np.array([0, -1.85, -1 / 9, -0.0823, -0.0415, 0])
        error_const = kappa * gamma + 1 / np.arange(1, max_order + 2)
        alpha = (1 - kappa) * gamma
        self.alpha = alpha
        min_factor = 0.2
        max_factor = 10

        self.D = self._init_D()

        # These arrays are fixed and only needs to be generated once.
        _I = []
        _J = []
        _U = []
        for i in range(1, self.order + 1):
            _I.append(np.arange(1, i + 1).reshape((i, 1)))
            _J.append(np.arange(1, i + 1))
            _U.append(calculate_R(_I[i-1], _J[i-1], i, 1))

        self._I = _I
        self._J = _J
        self._U = _U

        @__njit
        def norm(x):
            #return np.sum(x**2) / len(x) ** 0.5
            return np.linalg.norm(x) / len(x) ** 0.5

        #_lapack_cholesky = __njit(lapack_cholesky)

        if self.use_jit:
            lu_solve_ = __njit(lu_solve)
            _lu_factor = __njit(lu_factor)
            @__njit
            def lu_solve_wrapper(lu, ipiv, b):
                return lu_solve_(lu, ipiv, b.reshape(len(b), 1)).ravel()
        else:
            _lu_factor = lu_factor_scipy
            def lu_solve_wrapper(lu, ipiv, b):
                return lu_solve_scipy((lu, ipiv), b)

        _lu_solve = lu_solve_wrapper
        lu, ipiv = _lu_factor(np.array([[1.0, 0.0],[0.0, 1.0]]))
        _lu_solve(lu, ipiv, np.ones(2))
        self._lu_factor = _lu_factor

        @__njit
        def bdf_inner(interface: Interface, t, y_init, psi, c, scale, LU, ipiv):

            stat = 0
            # first estimate of next step

            # TODO: give last known derivative value, instead of calculating again
            y = y_init.copy()

            _iter = 0

            d = np.zeros_like(y)
            converged = False
            dy_norm_old = -1
            rate = 0

            for k in range(inner_itermax):
                _iter += 1
                interface.set_states(y)
                f = interface.get_deriv(t, y)
                b = c * f - psi - d
                dy = _lu_solve(LU, ipiv, b)
                dy_norm = norm(dy / scale)
                if k > 0:
                    rate = dy_norm / dy_norm_old

                    if rate >= 1 or rate ** (inner_itermax - k) / (1 - rate) * dy_norm > newton_tol:
                        stat = -1
                        break

                d += dy
                y += dy

                if dy_norm == 0 or (k > 0 and rate / (1 - rate) * dy_norm < newton_tol):
                    converged = True
                    break

                dy_norm_old = dy_norm

            return converged, rate, y, d, stat, _iter

        @__njit
        def bdf(interface: Interface, t, dt, y, _, __, _solve_state):
            n = len(y)
            ynew = np.empty_like(y)

            J = _solve_state[0]
            update_jacobian = _solve_state[1]
            LU = _solve_state[2]
            ipiv = _solve_state[3]
            updated = _solve_state[4]
            update_LU = _solve_state[5]
            jac_updates = _solve_state[6]
            D = _solve_state[7]
            dt_last = _solve_state[8]
            order = _solve_state[9]
            jacobian: Jacobian = _solve_state[10]
            _I = _solve_state[11]
            _J = _solve_state[12]
            _U = _solve_state[13]

            converged = False

            #  D contains the derivatives order 1, 2, ... up to 5. It must be updated if step size is changed.
            if dt != dt_last:
                update_D(_I, _J, _U, D, order, dt / dt_last)

            #  Dot product is similar to sum of np.sum(gamma[1:order+1] * D[1:order+1].T, axis=1)
            psi = 1 / alpha[order] * gamma[1:order + 1].dot(D[1:order + 1])

            y_init = np.sum(D[:order + 1], axis=0)  # euler integration using known derivatives

            scale = abs_tol + rel_tol * np.abs(y_init)
            c = dt / (alpha[order])
            t += dt

            d = np.empty_like(y)
            inner_iter = 0

            while not converged:

                # We need a smarter way to update the jacobian...
                if update_jacobian:
                    interface.set_states(y)
                    J = jacobian.get_jacobian(t)

                    update_jacobian = False
                    updated = True
                    update_LU = True
                    jac_updates += 1

                if update_LU:
                    jac = np.identity(n) - c * J
                    LU, ipiv = _lu_factor(jac)
                    update_LU = False

                converged, rate, ynew, d, stat, inner_iter = \
                    bdf_inner(interface, t, y_init, psi, c, scale, LU, ipiv)

                interface.set_states(ynew)

                if not converged:
                    if not updated:
                        update_jacobian = True
                    else:
                        update_LU = True
                        break

                if converged:
                    updated = False

            _solve_state = (J, update_jacobian, LU, ipiv, updated, update_LU, jac_updates, D, dt,
                            order, jacobian, _I, _J, _U)

            # print(t)
            if not converged:
                factor = shorter
                return t, ynew, converged, update_jacobian, _solve_state, factor

            safety = 0.9 * (2 * inner_itermax + 1) / (2 * inner_itermax + inner_iter)
            scale = abs_tol + rel_tol * np.abs(ynew)
            error = error_const[order] * d
            error_norm = norm(error / scale)
            if error_norm > 1:
                factor = max(min_factor, safety * error_norm ** (-1 / (order + 1)))
                converged = False
                return t, ynew, converged, update_jacobian, _solve_state, factor

            D[order + 2] = d - D[order + 1]
            D[order + 1] = d

            for i in np.arange(order + 1)[::-1]:
                D[i] += D[i + 1]

            if order > 1:
                error_m = error_const[order - 1] * D[order]
                error_m_norm = norm(error_m / scale)
            else:
                error_m_norm = np.inf

            if order < max_order:
                error_p = error_const[order + 1] * D[order + 2]
                error_p_norm = norm(error_p / scale)
            else:
                error_p_norm = np.inf

            error_norms = np.array([error_m_norm, error_norm, error_p_norm])
            factors = error_norms ** (-1 / np.arange(order, order + 3))

            delta_order = np.argmax(factors) - 1
            order += delta_order

            factor = min(max_factor, safety * max(factors))
            update_LU = True

            _solve_state = (J, update_jacobian, LU, ipiv, updated, update_LU, jac_updates, D, dt,
                            order, jacobian, _I, _J, _U)

            return t, ynew, converged, update_jacobian, _solve_state, factor

        self.step_func = bdf

    def _init_D(self):
        D = np.zeros((self.order + 3, len(self.y0)), dtype=np.float64)
        D[0] = self.y0
        D[1] = self.interface.get_deriv(0, self.y0) * self.initial_step
        return D

    def get_solver_state(self):
        n = len(self.y0)
        self.jac._jit(jit=self.use_jit)
        self.jac.reset()
        self.J = self.jac.get_jacobian(0)
        c = self.initial_step / (self.alpha[1])
        jac = np.identity(n) - c * self.J
        LU, ipiv = self._lu_factor(jac)
        self.D = self._init_D()


        #D_copy = self.D
        state = (self.J,
                 True,
                 LU,
                 ipiv,
                 False,
                 True,
                 0,
                 self.D,
                 self.initial_step,
                 1,
                 self.jac._compiled_model,
                 tuple(self._I),
                 tuple(self._J),
                 tuple(self._U)
                 )

        return state

class NoDiff(BaseMethod):
    """The method used when no model contains no derivatives.
    """
    def __init__(self, interface: Interface, use_jit: bool, **options):
        super(NoDiff, self).__init__(interface, use_jit, **options)
        self.order = 1
        self.initial_step = 0.001
        __njit = _njit(jit=self.use_jit)

        @__njit
        def _dummystep(interface: Interface, t: float, dt: float, y: list, yold: list, order: int, _solve_state: tuple):
            tnew = t+dt
            ynew = y
            step_info = 0

            return t+dt, ynew, True, step_info, _solve_state, 1e20

        self.step_func = _dummystep

    def get_solver_state(self):
        return (0,0)


class Euler(BaseMethod):
    """Implementation of an explicit first order euler method.
    """
    def __init__(self, interface: Interface, use_jit: bool, **options):
        super(Euler, self).__init__(interface, use_jit, **options)

        self.order = 1
        self.max_factor = options.get('max_factor', 10)
        self.atol = options.get('atol', 1e-3)
        self.rtol = options.get('rtol', 1e-3)

        self.y0 = interface.get_states()
        self.initial_step = select_initial_step(self.interface, 0, self.y0, 1, self.order, self.rtol,
                                                self.atol)

        def njit_(fun):
            if self.use_jit:
                return njit(fun)
            else:
                # return options['lp'](fun)
                return fun

        @njit_
        def euler(interface: Interface, t, dt, y, _not_used1, _not_used2, _solve_state):

            step_info = 1

            tnew = t + dt

            if len(y) == 0:
                return tnew, y, True, step_info, _solve_state, 1e20

            interface.set_states(y)
            fnew = interface.get_deriv(t, y)

            ynew = y + fnew * dt

            return tnew, ynew, True, step_info, _solve_state, 1e20

        self.step_func = euler

    def get_solver_state(self):
        return (0.0, 0.0, 0.0, self.max_factor, self.atol, self.rtol, 0.0, 1, self.order,
                1, True)
