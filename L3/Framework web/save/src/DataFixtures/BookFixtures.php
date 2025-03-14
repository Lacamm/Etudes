<?php

namespace App\DataFixtures;

use App\Entity\Book;
use DateTime;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Persistence\ObjectManager;


class BookFixtures extends Fixture
{
    public function load(ObjectManager $manager): void
    {
        for($i=1; $i<10; $i++){
            $book = new Book();
            $book->setTitle("Titre du livre n°$i")
            ->setPublisher("Maison d'édition du livre n°$i")
            ->setYear(2000+$i)
            ->setIsbn("Numéro ISBN du livre n°$i");
            $manager->persist($book);
        }
        $manager->flush();
    }
}
