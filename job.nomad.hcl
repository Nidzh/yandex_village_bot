job "yandex_village_bot_back" {
  datacenters = ["dc1"]
  type = "service"
  meta = {
    "version" = "0.0.11"
  }

  group "yandex_village_bot_back-group" {

    count = 1

    network {
      port "http" {
        static = 9500
      }
    }

    task "yandex_village_bot_back-task" {

      driver = "docker"

      template {
        data        = <<EOT
        GITHUB_TOKEN={{ with nomadVar "nomad/jobs" }}{{ .GITHUB_TOKEN }}{{ end }}
        GITHUB_USERNAME={{ with nomadVar "nomad/jobs" }}{{ .GITHUB_USERNAME	}}{{ end }}
        POSTGRESQL__HOST={{ with nomadVar "nomad/jobs" }}{{ .POSTGRES_HOST	}}{{ end }}
        POSTGRESQL__PORT={{ with nomadVar "nomad/jobs" }}{{ .POSTGRES_PORT	}}{{ end }}
        POSTGRESQL__USER={{ with nomadVar "nomad/jobs" }}{{ .POSTGRES_USER	}}{{ end }}
        POSTGRESQL__PASSWORD={{ with nomadVar "nomad/jobs" }}{{ .POSTGRES_PASSWORD	}}{{ end }}
        REDIS__HOST={{ with nomadVar "nomad/jobs" }}{{ .REDIS_HOST }}{{ end }}
        REDIS__PORT={{ with nomadVar "nomad/jobs" }}{{ .REDIS_PORT }}{{ end }}
        REDIS__USER={{ with nomadVar "nomad/jobs" }}{{ .REDIS_USER }}{{ end }}
        REDIS__PASSWORD={{ with nomadVar "nomad/jobs" }}{{ .REDIS_PASSWORD }}{{ end }}
        BOT__TOKEN={{ with nomadVar "nomad/jobs" }}{{ .YANDEX_VILLAGE_BOT_TOKEN }}{{ end }}

        EOT
        destination = "secrets/env.sh"
        env         = true
      }

      env {
        CONFIG__DEBUG         = "False"
        CONFIG__DEV_ENV       = "production"
        CONFIG__LOG_LEVEL     = "info"
        CONFIG__HOST          = "0.0.0.0"
        CONFIG__PORT          = 9500
        CONFIG__WORKERS_COUNT = 1

        SCHEDULER__RUN        = "True"
        REDIS__DATABASE       = 1
        POSTGRESQL__DATABASE  = "yandex_village"


        BOT__RUN              = "True"
        BOT__WEBHOOK_URL      = "https://village.baza.baby"
        BOT__WEBHOOK_IP       = "116.203.119.236"
        BOT__NAME             = "vertical_openair_bot"
      }

      config {
        image = "https://ghcr.io/nidzh/yandex_village_bot:latest" #  <<< ПУТЬ К КОНТЕЙНЕРУ
        ports = ["http"]
        force_pull = true
        auth = {
          username = "${GITHUB_USERNAME}"
          password = "${GITHUB_TOKEN}"
        }
      }


      resources {
        cpu    = 1000
        memory = 1024
      }
    }
  }
}
