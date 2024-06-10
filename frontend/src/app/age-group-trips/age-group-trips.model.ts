export interface AgeGroup {
    id: number;
    age: string;
}

export class Voyage { /*Se tiene que hacer una clase para poder instanciar cada viaje*/
    id: number = 0;
    city__name: string = '';
    date_start: string = '';
    date_end: string = '';
    description: string = '';
    itinerary: string = '';
    price: number = 0;
    active_travelers: number = 0;
    maximum_travelers: number = 0;
    age_group: string = '';
}