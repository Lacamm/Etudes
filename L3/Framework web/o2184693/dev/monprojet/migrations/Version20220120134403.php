<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20220120134403 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql('CREATE TABLE author (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname VARCHAR(255) DEFAULT NULL, lastname VARCHAR(255) NOT NULL)');
        $this->addSql('CREATE TEMPORARY TABLE __temp__book AS SELECT id, title, publisher, year, isbn, back_cover, cover FROM book');
        $this->addSql('DROP TABLE book');
        $this->addSql('CREATE TABLE book (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title VARCHAR(255) NOT NULL COLLATE BINARY, publisher VARCHAR(255) NOT NULL COLLATE BINARY, year DATE NOT NULL, isbn VARCHAR(255) NOT NULL, back_cover VARCHAR(255) DEFAULT NULL COLLATE BINARY, cover BOOLEAN DEFAULT NULL)');
        $this->addSql('INSERT INTO book (id, title, publisher, year, isbn, back_cover, cover) SELECT id, title, publisher, year, isbn, back_cover, cover FROM __temp__book');
        $this->addSql('DROP TABLE __temp__book');
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->addSql('DROP TABLE author');
        $this->addSql('CREATE TEMPORARY TABLE __temp__book AS SELECT id, title, publisher, year, isbn, back_cover, cover FROM book');
        $this->addSql('DROP TABLE book');
        $this->addSql('CREATE TABLE book (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title VARCHAR(255) NOT NULL, publisher VARCHAR(255) NOT NULL, year DATE NOT NULL, isbn INTEGER NOT NULL, back_cover VARCHAR(255) DEFAULT NULL, cover BOOLEAN DEFAULT NULL)');
        $this->addSql('INSERT INTO book (id, title, publisher, year, isbn, back_cover, cover) SELECT id, title, publisher, year, isbn, back_cover, cover FROM __temp__book');
        $this->addSql('DROP TABLE __temp__book');
    }
}
