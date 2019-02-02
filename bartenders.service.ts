import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

export interface Bartender{
  bar_tender: string;
  bar_name: string;
  shift: number;
  beer: string;
  selling: number;
}

@Injectable({
  providedIn: 'root'
})
export class BartendersService {

  constructor(
    public http: HttpClient
  ) { }

  getTenders(){
    return this.http.get<Bartender[]>('/api/bartender')
  }

  getBarTen(bartender?: string):any{
    if(bartender){
      return this.http.get<string>(`/api/bartender-tender/${bartender}`)
    }
    return this.http.get<string[]>('/api/bartender-tender')

  }
  getBbar(bartender?: string):any{
    if(bartender){
      return this.http.get<string>(`/api/bartender-bar/${bartender}`)
    }
    return this.http.get<string[]>('/api/bartender-bar')
    }
  }
