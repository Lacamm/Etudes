<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20220113142502 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql('ALTER TABLE book ADD COLUMN back_cover VARCHAR(255) DEFAULT NULL');
        $this->addSql('ALTER TABLE book ADD COLUMN cover BOOLEAN DEFAULT NULL');
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->addSql('CREATE TEMPORARY TABLE __temp__book AS SELECT id, title, publisher, year, isbn FROM book');
        $this->addSql('DROP TABLE book');
        $this->addSql('CREATE TABLE book (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title VARCHAR(255) NOT NULL, publisher VARCHAR(255) NOT NULL, year DATE NOT NULL, isbn INTEGER NOT NULL)');
        $this->addSql('INSERT INTO book (id, title, publisher, year, isbn) SELECT id, title, publisher, year, isbn FROM __temp__book');
        $this->addSql('DROP TABLE __temp__book');
    }
}
