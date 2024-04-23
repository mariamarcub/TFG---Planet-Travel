export class UserLogin {
    constructor(
      public username: string,
      public password: string
    ) {}
  }


export class UserRegister {
    constructor(
      public username: string,
      public first_name: string,
      public last_name: string,
      public password: string,
      public password2: string,
      public email: string
    ) {}
  }
  