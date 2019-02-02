import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { WelcomeComponent } from './welcome/welcome.component';
import { BarDetailsComponent } from './bar-details/bar-details.component';
import { BeerDetailsComponent } from './beer-details/beer-details.component';
import { BeersComponent } from './beers/beers.component';
import { InsightComponent } from './insight/insight.component';
import { BartendersComponent } from './bartenders/bartenders.component';

const routes: Routes = [
  {
    path:'',
    pathMatch:'full',
    redirectTo: 'bars'
  },
  {
    path:'bars',
    pathMatch:'full',
    component: WelcomeComponent
  },
  {
    path: 'bars/:bar',
    pathMatch: 'full',
    component: BarDetailsComponent
  },
  {
    path: 'beers',
    pathMatch: 'full',
    component: BeersComponent
  },
  {
    path:'beers/:beer',
    pathMatch:'full',
    component: BeerDetailsComponent
  },
  {
    path: 'insight',
    pathMatch:'full',
    component: InsightComponent
  },
  {
    path: 'bartenders',
    pathMatch: 'full',
    component: BartendersComponent
  }


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
