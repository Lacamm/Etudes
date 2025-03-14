class Author{
  private _firstname:string;
  private _lastname:string;
  private _id:number;


  constructor(firstname: string, lastname: string, id: number) {
    this._firstname = firstname;
    this._lastname = lastname;
    this._id = id;
  }


  get firstname(): string {
    return this._firstname;
  }

  set firstname(value: string) {
    this._firstname = value;
  }

  get lastname(): string {
    return this._lastname;
  }

  set lastname(value: string) {
    this._lastname = value;
  }

  get id(): number {
    return this._id;
  }

  set id(value: number) {
    this._id = value;
  }
}
