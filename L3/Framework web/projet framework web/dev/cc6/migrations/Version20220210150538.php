<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20220210150538 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->addSql('CREATE TABLE activite (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, animateur_id INTEGER NOT NULL, creator_id INTEGER NOT NULL, nom VARCHAR(100) NOT NULL, description VARCHAR(255) NOT NULL)');
        $this->addSql('CREATE INDEX IDX_B87555157F05C301 ON activite (animateur_id)');
        $this->addSql('CREATE INDEX IDX_B875551561220EA6 ON activite (creator_id)');
        $this->addSql('CREATE TABLE activite_user (activite_id INTEGER NOT NULL, user_id INTEGER NOT NULL, PRIMARY KEY(activite_id, user_id))');
        $this->addSql('CREATE INDEX IDX_FA43CF3B9B0F88B1 ON activite_user (activite_id)');
        $this->addSql('CREATE INDEX IDX_FA43CF3BA76ED395 ON activite_user (user_id)');
        $this->addSql('CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nom VARCHAR(50) NOT NULL, prenom VARCHAR(50) NOT NULL, email VARCHAR(180) NOT NULL, roles CLOB NOT NULL --(DC2Type:json)
        , password VARCHAR(255) NOT NULL)');
        $this->addSql('CREATE UNIQUE INDEX UNIQ_8D93D649E7927C74 ON user (email)');
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->addSql('DROP TABLE activite');
        $this->addSql('DROP TABLE activite_user');
        $this->addSql('DROP TABLE user');
    }
}
