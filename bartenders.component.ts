import { Bartender, BartendersService } from './../bartenders.service';
import { Component, OnInit } from '@angular/core';
import { SelectItem } from 'primeng/components/common/selectitem';

@Component({
  selector: 'app-bartenders',
  templateUrl: './bartenders.component.html',
  styleUrls: ['./bartenders.component.css']
})
export class BartendersComponent implements OnInit {

  bartenders : any[];
  originalBartender: any[];
  tenderOptions: SelectItem[];
  barOptions: SelectItem[];

  constructor(
    public bartenderService: BartendersService
  ) {
    this.getTenders();
    this.bartenderService.getBarTen().subscribe(
      data => {
        this.tenderOptions = data.map(bar_tender => {
          return {
            label: bar_tender,
            value: bar_tender,
          }
        })
      }
    )
    this.bartenderService.getBbar().subscribe(
      data => {
        this.barOptions = data.map(bar_name => {
          return{
            label: bar_name,
            value: bar_name,
          }
        })
      }
    )
   }

  ngOnInit() {
  }

  getTenders(){
    this.bartenderService.getTenders().subscribe(
      data =>{
        this.bartenders = data;
        this.originalBartender = data;
      },
      error =>{
        alert('Could not retreive a list of drinkers');
      }
    );
  }
  

  filterBars(Bartender:string){
      this.bartenders = this.originalBartender;
      if(Bartender){
        this.bartenders = this.originalBartender.filter(bartender => bartender.bar_tender === Bartender);
      }
  }

  filterTenders(Bartender:string){
    this.bartenders = this.originalBartender;
    if(Bartender){
      this.bartenders = this.originalBartender.filter(bartender => bartender.bar_name === Bartender);
    }
  }

}
