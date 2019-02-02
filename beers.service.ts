import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface BeerLocation {
  bar: string;
  price: number;
  customers: number;
}

export interface Beersell{
  bar: string;
  selling:number;
}

export interface Rich{
  last_name: string;
  money: number;
}

@Injectable({
  providedIn: 'root'
})
export class BeersService {

  constructor(private http: HttpClient) { }

  getBeers() {
    return this.http.get<any[]>('/api/beer');
  }

  getBarsSelling(beer: string) {
    return this.http.get<BeerLocation[]>(`/api/bars-selling/${beer}`);
  }

  getBeerSelling(beer: string){
    return this.http.get<Beersell[]>(`/api/beer-selling/${beer}`);
  }

  getRichPeople(beer: string){
    return this.http.get<Rich[]>(`/api/beer-rich/${beer}`);
  }

  getBeerManufacturers(beer?: string): any {
    if (beer) {
      return this.http.get<string>(`/api/beer-manufacturer/${beer}`);
    }
    return this.http.get<string[]>('/api/beer-manufacturer');
  }

}