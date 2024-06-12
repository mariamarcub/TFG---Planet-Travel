import { Component, OnInit } from '@angular/core';
import { OpinionService } from './opinion.service';
import { Opinion } from './opinion.model';

@Component({
  selector: 'app-opinion',
  templateUrl: './opinion.component.html',
  styleUrls: ['./opinion.component.css']
})
export class OpinionComponent implements OnInit {
  opinions: Opinion[] = [];
  currentOpinions: Opinion[] = [];

  constructor(private opinionService: OpinionService) {}

  ngOnInit() {
    // Obtener opiniones al iniciar el componente
    this.getOpinions();

    // Actualizar las opiniones cada 5 minutos (300000 ms)
    setInterval(() => {
      this.getOpinions();
    }, 10000);
  }


  //Coge las opiniones almacenadas
  getOpinions() {
    this.opinionService.getOpinions().subscribe(
      (opinions: Opinion[]) => {
        this.opinions = opinions;
        this.updateCurrentOpinions(); //Llamamos al método que actualiza las opiniones que se muestran
      }
    );
  }

  //Actualiza las 5 opiniones que se mostrarán 
  updateCurrentOpinions() {
    if (this.opinions.length > 0) {
      // Obtener cinco opiniones aleatorias
      const randomIndices = this.getRandomIndices(this.opinions.length, 5); //Selecciona 5 opiniones aleatoriamente
      this.currentOpinions = randomIndices.map(index => this.opinions[index]); //Las añade en un nuevo mapa para mostrarlas
    }
  }

  //Para evitar que salgan aleatorios idénticos.
  getRandomIndices(max: number, count: number): number[] {
    const indices: number[] = []; //Guardaremos índices aleatorios
    while (indices.length < count) {
      const randomIndex = Math.floor(Math.random() * max); //Se genera un nuevo índice aleatorio en cada iteración. Se usa el Math.floor para que sea un número entero
      if (!indices.includes(randomIndex)) { //Si no está incluido dicho índice
        indices.push(randomIndex); //Se introduce
      }
    }
    return indices; //Devuelve el array con las nuevas opiniones
  }

  // Método para convertir el rating numérico en estrellas
  convertToStars(rating: number): string {
    let stars = '';
    for (let i = 0; i < rating; i++) { //Recorremos el rating del 1 al 5, que son el número de estrellas que hay disponibles
      stars += '★'; // Añade una estrella al string de estrellas
    }
    return stars;
  }

}
