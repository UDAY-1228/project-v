import { State, Action, StateContext, Selector } from '@ngxs/store';
import { Injectable } from '@angular/core';
import { Institution } from '../../models';

export interface InstitutionStateModel {
  current: Institution | null;
  list: Institution[];
}

export class SetCurrentInstitution {
  static readonly type = '[Institution] Set Current';
  constructor(public payload: Institution) {}
}

export class SetInstitutionList {
  static readonly type = '[Institution] Set List';
  constructor(public payload: Institution[]) {}
}

@State<InstitutionStateModel>({
  name: 'institution',
  defaults: { current: null, list: [] },
})
@Injectable()
export class InstitutionState {
  @Selector() static current(state: InstitutionStateModel) { return state.current; }
  @Selector() static list(state: InstitutionStateModel) { return state.list; }

  @Action(SetCurrentInstitution)
  setCurrent(ctx: StateContext<InstitutionStateModel>, action: SetCurrentInstitution) {
    ctx.patchState({ current: action.payload });
  }

  @Action(SetInstitutionList)
  setList(ctx: StateContext<InstitutionStateModel>, action: SetInstitutionList) {
    ctx.patchState({ list: action.payload });
  }
}
