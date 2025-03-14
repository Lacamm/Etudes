<?php

namespace App\Entity;

use App\Repository\CoverRepository;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: CoverRepository::class)]
class Cover
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column(type: 'integer')]
    private $id;

    #[ORM\Column(type: 'string', length: 255)]
    private $ibsn;

    #[ORM\Column(type: 'string', length: 255)]
    private $caption;

    #[ORM\Column(type: 'integer')]
    private $date;

    #[ORM\Column(type: 'string', length: 255)]
    private $source;

    #[ORM\Column(type: 'string', length: 255)]
    private $license;

    #[ORM\Column(type: 'string', length: 255)]
    private $filename;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getIbsn(): ?string
    {
        return $this->ibsn;
    }

    public function setIbsn(string $ibsn): self
    {
        $this->ibsn = $ibsn;

        return $this;
    }

    public function getCaption(): ?string
    {
        return $this->caption;
    }

    public function setCaption(string $caption): self
    {
        $this->caption = $caption;

        return $this;
    }

    public function getDate(): ?int
    {
        return $this->date;
    }

    public function setDate(int $date): self
    {
        $this->date = $date;

        return $this;
    }

    public function getSource(): ?string
    {
        return $this->source;
    }

    public function setSource(string $source): self
    {
        $this->source = $source;

        return $this;
    }

    public function getLicense(): ?string
    {
        return $this->license;
    }

    public function setLicense(string $license): self
    {
        $this->license = $license;

        return $this;
    }

    public function getFilename(): ?string
    {
        return $this->filename;
    }

    public function setFilename(string $filename): self
    {
        $this->filename = $filename;

        return $this;
    }
}
