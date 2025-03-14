
class Book{
  private _name: string;
  private _isbn: number;
  private _auteur: Author;


  constructor(name: string, isbn: number, auteur: Author) {
    this._name = name;
    this._isbn = isbn;
    this._auteur = auteur;
  }


  get name(): string {
    return this._name;
  }

  set name(value: string) {
    this._name = value;
  }

  get isbn(): number {
    return this._isbn;
  }

  set isbn(value: number) {
    this._isbn = value;
  }

  get auteur(): Author {
    return this._auteur;
  }

  set auteur(value: Author) {
    this._auteur = value;
  }
}

