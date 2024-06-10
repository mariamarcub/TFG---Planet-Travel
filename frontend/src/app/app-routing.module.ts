import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CabeceraComponent } from './cabecera/cabecera.component';
import { LoginComponent } from './login/login.component';
import { MonthTripsComponent } from './month-trips/month-trips.component';
import { ProfileComponent } from './profile/profile.component';
import { VoyageComponent } from './voyage/voyage.component';
import { BookingComponent } from './booking/booking.component';
import { DestinyComponent } from './destiny/destiny.component';
import { BodyComponent } from './body/body.component';
import { IndexComponent } from './index/index.component';
import { ForumComponent } from './forum/forum.component';
import { AgeGroupTripsComponent } from './age-group-trips/age-group-trips.component';
import { ThreadForumComponent } from './thread-forum/thread-forum.component';
import { LoginGuard } from './login/login.guard'; // Llamamos al Guard para poder hacer privadas determinadas páginas


const routes: Routes = [
  { path: '', component: IndexComponent },
  { path: 'login', component: LoginComponent }, //Definimos la ruta para poder ir al HTML del componente login
  { path: 'monthTrips/:month', component: MonthTripsComponent },//Definimos la ruta para poder visualizar los viajes por meses  
  { path: 'countries/:des', component: DestinyComponent }, //Definimos la ruta para ver todos los viajes filtrados por continentes
  { path: 'ageGroup/:ageGroup', component: AgeGroupTripsComponent}, //Definimos la ruta para ver todos los viajes filtrados por grupo de edad
  { path: 'profile', component: ProfileComponent, canActivate: [LoginGuard] },
  { path: 'showVoyage/:voyage', component: VoyageComponent },
  { path: 'bookingVoyage/:voyage', component: BookingComponent, canActivate: [LoginGuard] }, //Solo tienen acceso los usuarios registrados
  { path: 'continentTrips/:continent', component: DestinyComponent },
  { path: 'forumVoyage/:voyage', component: ForumComponent },
  { path: 'forumVoyage/thread/:thread', component: ThreadForumComponent },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }