job "#########" {
  datacenters = ["dc1"]
  type = "service"
  meta = {
    "version" = "0.0.1"
  }

  group "#########" {

    count = 1

    network {
      port "http" {
        static = 0000
      }
    }

    task "#########" {

      driver = "docker"

      template {
        data        = <<EOT

        GITHUB_TOKEN={{ with nomadVar "nomad/jobs" }}{{ .GITHUB_TOKEN }}{{ end }}
        GITHUB_USERNAME={{ with nomadVar "nomad/jobs" }}{{ .GITHUB_USERNAME	}}{{ end }}

        EOT
        destination = "secrets/env.sh"
        env         = true
      }

      env {
        DEV_ENV     = "PRODUCTION"
      }

      config {
        image = "https://ghcr.io/nidzh/##########
        ports = ["http"]
        force_pull = true
        auth = {
          username = "${GITHUB_USERNAME}"
          password = "${GITHUB_TOKEN}"
        }
      }


      resources {
        cpu    = 500
        memory = 512
      }
    }
  }
}