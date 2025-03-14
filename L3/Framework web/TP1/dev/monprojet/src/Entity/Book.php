<?php

namespace App\Entity;

use App\Repository\BookRepository;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: BookRepository::class)]
class Book
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column(type: 'integer')]
    private $id;

    #[ORM\Column(type: 'string', length: 255)]
    private $title;

    #[ORM\Column(type: 'string', length: 255)]
    private $publisher;

    #[ORM\Column(type: 'date')]
    private $year;

    #[ORM\Column(type: 'integer')]
    private $isbn;

    #[ORM\Column(type: 'string', length: 255, nullable: true)]
    private $back_cover;

    #[ORM\Column(type: 'boolean', nullable: true)]
    private $cover;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getTitle(): ?string
    {
        return $this->title;
    }

    public function setTitle(string $title): self
    {
        $this->title = $title;

        return $this;
    }

    public function getPublisher(): ?string
    {
        return $this->publisher;
    }

    public function setPublisher(string $publisher): self
    {
        $this->publisher = $publisher;

        return $this;
    }

    public function getYear(): ?\DateTimeInterface
    {
        return $this->year;
    }

    public function setYear(\DateTimeInterface $year): self
    {
        $this->year = $year;

        return $this;
    }

    public function getIsbn(): ?string
    {
        return $this->isbn;
    }

    public function setIsbn(string $isbn): self
    {
        $this->isbn = $isbn;

        return $this;
    }

    public function getBackCover(): ?string
    {
        return $this->back_cover;
    }

    public function setBackCover(?string $back_cover): self
    {
        $this->back_cover = $back_cover;

        return $this;
    }

    public function getCover(): ?bool
    {
        return $this->cover;
    }

    public function setCover(?bool $cover): self
    {
        $this->cover = $cover;

        return $this;
    }
}
