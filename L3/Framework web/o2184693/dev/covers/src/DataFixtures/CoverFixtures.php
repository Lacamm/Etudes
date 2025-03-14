<?php

namespace App\DataFixtures;

use App\Entity\Cover;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Persistence\ObjectManager;

class CoverFixtures extends Fixture
{
    public function load(ObjectManager $manager): void
    {
        for($i=1; $i<10; $i++){
            $cover = new Cover();
            $cover->setFilename("Nom de la cover n°$i")
                ->setIbsn("Numéro ISBN du livre n°$i")
                ->setCaption("Description de la cover n°$i")
                ->setSource("Source de la cover n°$i")
                ->setLicense("Licence d'utilisation de la cover n°$i")
                ->setDate(2000+$i);
            $manager->persist($cover);
        }
        $manager->flush();
    }
}
