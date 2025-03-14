<?php

namespace App\DataFixtures;

use App\Entity\Author;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Persistence\ObjectManager;

class AuthorFixtures extends Fixture
{
    public function load(ObjectManager $manager): void
    {
        for($i=1; $i<5; $i++){
            $author = new Author();
            $author->setFirstname("Prénom  de l'auteur n°$i")
                ->setLastname("Nom de l'auteur n°$i");
            $manager->persist($author);
        }
        $manager->flush();
    }
}
