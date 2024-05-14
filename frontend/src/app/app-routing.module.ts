import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CabeceraComponent } from './cabecera/cabecera.component';
import { LoginComponent } from './login/login.component';
import { MonthTripsComponent } from './month-trips/month-trips.component';
import { ProfileComponent } from './profile/profile.component';
import { VoyageComponent } from './voyage/voyage.component';


const routes: Routes = [
  { path: '', component: CabeceraComponent },
  { path: 'login', component: LoginComponent }, //Definimos la ruta para poder ir al HTML del componente login
  { path: 'monthTrips/:month', component: MonthTripsComponent },//Definimos la ruta para poder visualizar los viajes por meses
  { path: 'profile', component: ProfileComponent },
  { path: 'showVoyage/:voyage', component: VoyageComponent },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
