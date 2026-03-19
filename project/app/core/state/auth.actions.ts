import { TokenResponse, User } from '../../models';

export class Login {
  static readonly type = '[Auth] Login';
  constructor(public payload: TokenResponse) {}
}

export class Logout {
  static readonly type = '[Auth] Logout';
}

export class SetUser {
  static readonly type = '[Auth] Set User';
  constructor(public payload: User) {}
}
