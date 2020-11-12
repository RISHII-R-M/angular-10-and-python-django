import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SharedService {
readonly APIUrl = "http://127.0.0.1:8000";


  constructor(private http:HttpClient) { }

  getPartaList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/parta/');
  }

  addParta(val:any){
    return this.http.post(this.APIUrl + '/parta/',val);
  }

  updateParta(val:any){
    return this.http.put(this.APIUrl + '/parta/',val);
  }

  deleteparta(val:any){
    return this.http.delete(this.APIUrl + '/parta/'+val);
  }


  getPartbList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/partb/');
  }

  addPartb(val:any){
    return this.http.post(this.APIUrl + '/partb/',val);
  }

  updatePartb(val:any){
    return this.http.put(this.APIUrl + '/partb/',val);
  }

  deletePartb(val:any){
    return this.http.delete(this.APIUrl + '/partb/'+val);
  }

 

  getAllPartaNames():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/parta/');
  }


}
