export interface Destiny {
    id: number;
    date: Date;
}

export class Continent {
  id: number;
  name: string;
  selectedContinentName: boolean; // Propiedad para indicar si este continente está seleccionado

}

export class Voyage {
    id: number = 0;
    city: {
      name: string;
    } = { name: '' };
    date_start: string = '';
    date_end: string = '';
    description: string = '';
    itinerary: string = '';
    price: number = 0;
    active_travelers: number = 0;
    maximum_travelers: number = 0;
    age_group: string = '';
  }
  