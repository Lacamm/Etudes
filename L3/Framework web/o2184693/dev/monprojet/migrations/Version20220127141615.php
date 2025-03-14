<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20220127141615 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql('CREATE TEMPORARY TABLE __temp__book AS SELECT id, title, publisher, year, isbn, back_cover, cover FROM book');
        $this->addSql('DROP TABLE book');
        $this->addSql('CREATE TABLE book (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title VARCHAR(255) NOT NULL COLLATE BINARY, publisher VARCHAR(255) NOT NULL COLLATE BINARY, year INTEGER NOT NULL, isbn VARCHAR(255) NOT NULL COLLATE BINARY, back_cover VARCHAR(255) DEFAULT NULL COLLATE BINARY, cover BOOLEAN DEFAULT NULL)');
        $this->addSql('INSERT INTO book (id, title, publisher, year, isbn, back_cover, cover) SELECT id, title, publisher, year, isbn, back_cover, cover FROM __temp__book');
        $this->addSql('DROP TABLE __temp__book');
        $this->addSql('DROP INDEX IDX_9478D34516A2B381');
        $this->addSql('DROP INDEX IDX_9478D345F675F31B');
        $this->addSql('CREATE TEMPORARY TABLE __temp__book_author AS SELECT book_id, author_id FROM book_author');
        $this->addSql('DROP TABLE book_author');
        $this->addSql('CREATE TABLE book_author (book_id INTEGER NOT NULL, author_id INTEGER NOT NULL, PRIMARY KEY(book_id, author_id), CONSTRAINT FK_9478D34516A2B381 FOREIGN KEY (book_id) REFERENCES book (id) ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE, CONSTRAINT FK_9478D345F675F31B FOREIGN KEY (author_id) REFERENCES author (id) ON DELETE CASCADE NOT DEFERRABLE INITIALLY IMMEDIATE)');
        $this->addSql('INSERT INTO book_author (book_id, author_id) SELECT book_id, author_id FROM __temp__book_author');
        $this->addSql('DROP TABLE __temp__book_author');
        $this->addSql('CREATE INDEX IDX_9478D34516A2B381 ON book_author (book_id)');
        $this->addSql('CREATE INDEX IDX_9478D345F675F31B ON book_author (author_id)');
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->addSql('CREATE TEMPORARY TABLE __temp__book AS SELECT id, title, publisher, year, isbn, back_cover, cover FROM book');
        $this->addSql('DROP TABLE book');
        $this->addSql('CREATE TABLE book (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title VARCHAR(255) NOT NULL, publisher VARCHAR(255) NOT NULL, year DATE NOT NULL, isbn VARCHAR(255) NOT NULL, back_cover VARCHAR(255) DEFAULT NULL, cover BOOLEAN DEFAULT NULL)');
        $this->addSql('INSERT INTO book (id, title, publisher, year, isbn, back_cover, cover) SELECT id, title, publisher, year, isbn, back_cover, cover FROM __temp__book');
        $this->addSql('DROP TABLE __temp__book');
        $this->addSql('DROP INDEX IDX_9478D34516A2B381');
        $this->addSql('DROP INDEX IDX_9478D345F675F31B');
        $this->addSql('CREATE TEMPORARY TABLE __temp__book_author AS SELECT book_id, author_id FROM book_author');
        $this->addSql('DROP TABLE book_author');
        $this->addSql('CREATE TABLE book_author (book_id INTEGER NOT NULL, author_id INTEGER NOT NULL, PRIMARY KEY(book_id, author_id))');
        $this->addSql('INSERT INTO book_author (book_id, author_id) SELECT book_id, author_id FROM __temp__book_author');
        $this->addSql('DROP TABLE __temp__book_author');
        $this->addSql('CREATE INDEX IDX_9478D34516A2B381 ON book_author (book_id)');
        $this->addSql('CREATE INDEX IDX_9478D345F675F31B ON book_author (author_id)');
    }
}
