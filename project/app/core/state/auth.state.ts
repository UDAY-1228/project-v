import { State, Action, StateContext, Selector } from '@ngxs/store';
import { Injectable } from '@angular/core';
import { User, UserRole, TokenResponse } from '../../models';
import { Login, Logout, SetUser } from './auth.actions';

export interface AuthStateModel {
  token: string | null;
  refreshToken: string | null;
  user: User | null;
  role: UserRole | null;
  isAuthenticated: boolean;
}

@State<AuthStateModel>({
  name: 'auth',
  defaults: {
    token: localStorage.getItem('eims_token'),
    refreshToken: localStorage.getItem('eims_refresh_token'),
    user: JSON.parse(localStorage.getItem('eims_user') || 'null'),
    role: localStorage.getItem('eims_role') as UserRole | null,
    isAuthenticated: !!localStorage.getItem('eims_token'),
  },
})
@Injectable()
export class AuthState {
  @Selector() static token(state: AuthStateModel) { return state.token; }
  @Selector() static user(state: AuthStateModel) { return state.user; }
  @Selector() static role(state: AuthStateModel) { return state.role; }
  @Selector() static isAuthenticated(state: AuthStateModel) { return state.isAuthenticated; }

  @Action(Login)
  login(ctx: StateContext<AuthStateModel>, action: Login) {
    const { access_token, refresh_token, role, user } = action.payload;
    localStorage.setItem('eims_token', access_token);
    localStorage.setItem('eims_refresh_token', refresh_token);
    localStorage.setItem('eims_role', role);
    localStorage.setItem('eims_user', JSON.stringify(user));
    ctx.patchState({ token: access_token, refreshToken: refresh_token, user, role, isAuthenticated: true });
  }

  @Action(Logout)
  logout(ctx: StateContext<AuthStateModel>) {
    localStorage.removeItem('eims_token');
    localStorage.removeItem('eims_refresh_token');
    localStorage.removeItem('eims_role');
    localStorage.removeItem('eims_user');
    ctx.patchState({ token: null, refreshToken: null, user: null, role: null, isAuthenticated: false });
  }

  @Action(SetUser)
  setUser(ctx: StateContext<AuthStateModel>, action: SetUser) {
    localStorage.setItem('eims_user', JSON.stringify(action.payload));
    ctx.patchState({ user: action.payload });
  }
}
