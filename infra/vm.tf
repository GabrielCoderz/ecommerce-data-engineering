resource "google_compute_instance" "pipeline-engine" {
  name         = "pipeline-engine"
  machine_type = "e2-small"
  zone         = "us-central1-a"

  tags = ["allow-mage-ai"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = file("startup-script.sh")
}

resource "google_compute_disk" "default" {
  name  = "test-disk"
  type  = "pd-ssd"
  zone  = "us-central1-a"
  image = "debian-11-bullseye-v20220719"
  size = 10
  labels = {
    environment = "dev"
  }

}

resource "google_compute_firewall" "allow_mage_ai" {
  name    = "allow-mage-ai"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["6789"]
  }

  source_ranges = ["201.4.138.65"]
  target_tags   = ["allow-mage-ai"]
}