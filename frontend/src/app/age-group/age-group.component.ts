import { Component, OnInit } from '@angular/core';
import { AgeGroupService } from './age-group.service';
import { AgeGroup } from './age-group.model';
import { Router } from '@angular/router';


@Component({
  selector: 'app-age-group',
  templateUrl: './age-group.component.html',
  styleUrls: ['./age-group.component.css']
})

export class AgeGroupComponent implements OnInit {
  ageGroup: AgeGroup[] = [];

  constructor(private AgeGroupService: AgeGroupService, private router: Router) {}

  ngOnInit() {
    this.ageGroup = [
      new AgeGroup(1, '18-30'),
      new AgeGroup(2, '30-45'),
      new AgeGroup(3, '45+')
    ];
  }

  viewVoyagesAge(ageGroup: string){
    this.router.navigate(['/ageGroup', ageGroup]) /*Me dirige a la ruta deseada*/
  }
}
