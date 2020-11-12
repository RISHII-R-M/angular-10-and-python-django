import { Component, OnInit } from '@angular/core';
import {SharedService} from 'src/app/shared.service';
import { Chart, ChartDataSets, ChartOptions, ChartType } from 'chart.js';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private service:SharedService) { }

 PartaList: any;
 PartbList: any=[];
year:any=[];
year1:any=[];
totalLoss:any=[];
totalIncome:any=[];

TotalExpenditure:any=[];
BookingScore:any=[];
 ngOnInit(): void {
this.refreshPartaList();
this.refreshPartbList();
}


chartData: ChartDataSets[] = [
  {
    data: []
  
    
  },
  {
    data: []
  
    
  }
];
	lineChartOptions: ChartOptions = {
		responsive: true,
		scales: {
			yAxes: [{
			  scaleLabel: {
				display: true,
				labelString: 'Income / Loss',
				fontSize: 20

			  },
			  ticks: {
				fontSize: 20
			}
			}],
			xAxes: [{
				scaleLabel: {
				  display: true,
				  labelString: ' Years',
				  fontSize: 20
				},
				ticks: {
					fontSize: 20
				}
			  }],

		  } 
	  };
chartLabels = [];

lineChartOptions1: ChartOptions = {
  responsive: true,
  scales: {
    yAxes: [{
      scaleLabel: {
      display: true,
      labelString: 'booking / expenditure',
      fontSize: 20

      },
      ticks: {
      fontSize: 20
    }
    }],
    xAxes: [{
      scaleLabel: {
        display: true,
        labelString: ' year ',
        fontSize: 20
      },
      ticks: {
        fontSize: 20
      }
      }],

    } 
  };
refreshPartaList(){
  this.service.getPartaList().subscribe(data=>{
   
    this.PartaList=data;


 this.year=data.map((item)=>{
return item.Year
 })
 this.totalIncome=data.map((item)=>{
  return item.TotalIncome
})
 this.totalLoss=data.map((item)=>{
  return item.TotalLoss
})

this.chartData = [{ data: this.totalIncome,label:"Total Income",fill:false,},
                 { data: this.totalLoss,label:'Total Loss',fill:false}];
            
     console.log(this.totalIncome);
      

  });
  
}





chartData1: ChartDataSets[] = [
  {
    data: []
  
    
  },
  {
    data: []
  
    
  }
];
refreshPartbList(){
  this.service.getPartbList().subscribe(data=>{
    this.PartbList=data;
    
    this.year1=data.map((item)=>{
      return item.Year
       })
       this.TotalExpenditure=data.map((item)=>{
        return item.TotalExpenditure
      })
       this.BookingScore=data.map((item)=>{
        return item.BookingScore
      })
      
      this.chartData1 = [{ data: this.TotalExpenditure,label:"Total Expenditure",fill:false,},
                       { data: this.BookingScore,label:'Booking Score',fill:false}];
  });
}



}