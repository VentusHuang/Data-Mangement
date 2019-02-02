import { Component, OnInit } from '@angular/core';
import{ ActivatedRoute } from '@angular/router';
import{ BarsService, Bar, BarMenuItem} from '../bars.service';
import { HttpResponse } from '@angular/common/http';

declare const Highcharts: any;

@Component({
  selector: 'app-bar-details',
  templateUrl: './bar-details.component.html',
  styleUrls: ['./bar-details.component.css']
})
export class BarDetailsComponent implements OnInit {

  barName: string;
  barDetails: Bar;
  
  menu: BarMenuItem[];


  constructor(
    private barService: BarsService,
    private route: ActivatedRoute
  ) { 
    route.paramMap.subscribe((paramMap) => {
      this.barName = paramMap.get('bar');

      barService.getBar(this.barName).subscribe(
        data => {
          this.barDetails = data;
        },
        (error: HttpResponse<any>) => {
          if (error.status === 404) {
            alert('Bar not found');
          }
          else{
            console.error(error.status + '-' + error.body);
            alert('An error occur, check console');
          }
        }
      );

      barService.getMenu(this.barName).subscribe(
        data => {
          this.menu = data;
        }
        
      )

      this.barService.get_top_sepender(this.barName).subscribe(
        data => {
          console.log(data);

          const name = [];
          const spend = [];

          data.forEach(bar => {
            name.push(bar.Last_name);
            spend.push(bar.spending);
          });

          this.renderChart(name,spend);
        }
      )

      this.barService.get_top_beer(this.barName).subscribe(
        data => {
          console.log(data);

          const namee = [];
          const spendd = [];

          data.forEach(bar => {
            namee.push(bar.beer);
            spendd.push(bar.times);
          });

          this.henderChart(namee,spendd);
        }
      )
    });
  }

  ngOnInit() {
  }

  renderChart(name: string[], spend:number[]){
    Highcharts.chart('bargraph',{
      chart:{
        type: 'column'
      },
      title: {
        text: 'Top 10 spender'
      },
      xAxis: {
        categories: name,
        title: {
          text: 'drinker'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'times of spend'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        bar: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend: {
        enabled: false
      },
      credits: {
        enabled: false
      },
      series: [{
        data: spend
      }]
    });
  }

  henderChart(namee: string[], spendd:number[]){
    Highcharts.chart('pargraph',{
      chart:{
        type: 'column'
      },
      title: {
        text: 'Top 10 beer'
      },
      xAxis: {
        categories: namee,
        title: {
          text: 'Beer'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'times of sell'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        bar: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend: {
        enabled: false
      },
      credits: {
        enabled: false
      },
      series: [{
        data: spendd
      }]
    });
  }

}
