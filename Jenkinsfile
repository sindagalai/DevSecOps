pipeline {
    agent any

    environment {
        SONAR_HOST_URL = 'http://192.168.33.10:9000'       // Serveur SonarQube
        SONAR_LOGIN = 'sqa_244ff31ac55a8fce14f02ea76075176e0ed54348'   // Token SonarQube
        IMAGE_NAME = 'devsecops-demo'                      // Nom de l’image Docker
    }

    stages {

        stage('Build') {
            steps {
                echo '🔨 Compilation et préparation du projet...'
                sh 'python3 -m py_compile test.py || true'
            }
        }

        stage('SAST - SonarQube') {
            steps {
                echo '🔎 Analyse statique du code avec SonarQube...'
                sh '''
                    /opt/sonar-scanner/bin/sonar-scanner \
                        -Dsonar.projectKey=DevSecOpsDemo \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=${SONAR_HOST_URL} \
                        -Dsonar.login=${SONAR_LOGIN} || true
                '''
            }
        }

        stage('SCA + Docker Scan - Trivy') {
            steps {
                echo '🧪 Analyse des dépendances et de l’image Docker avec Trivy...'
                sh '''
                    mkdir -p reports
                    chmod 777 reports
                    trivy fs . --scanners vuln --format json --output reports/trivy_sca_report.json || true
                    trivy fs . --scanners vuln --format table --output reports/trivy_sca_report.txt || true

                    docker build -t ${IMAGE_NAME}:latest .
                    trivy image ${IMAGE_NAME}:latest --format json --output reports/trivy_docker_report.json || true
                    trivy image ${IMAGE_NAME}:latest --format table --output reports/trivy_docker_report.txt || true
                '''
            }
        }

        stage('Secrets Scan - Gitleaks') {
            steps {
                echo '🔐 Détection de secrets dans le code (Gitleaks)...'
                sh '''
                    mkdir -p reports
                    chmod 777 reports
                    gitleaks detect --no-git --source . --report-path reports/gitleaks_report.json || true
                '''
            }
        }

        stage('DAST - OWASP ZAP') {
            steps {
                echo '🕵️ Test dynamique de sécurité (OWASP ZAP)...'
                sh '''
                    mkdir -p reports
                    chmod 777 reports
                    docker run --rm --network host \
                        -v "$(pwd)/reports:/zap/wrk/:rw" \
                        ghcr.io/zaproxy/zaproxy:stable \
                        zap-baseline.py -t https://juice-shop.herokuapp.com -r zap_report.html || true
                    mv zap_report.html reports/zap_report.html || true
                '''
            }
        }

        stage('Rapport Final') {
            steps {
                echo '📊 Compilation et archivage des rapports...'
                sh 'ls -lh reports/ || true'
                archiveArtifacts artifacts: 'reports/*.json, reports/*.html, reports/*.txt', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline terminé avec succès — tous les rapports ont été générés et archivés.'
        }
        failure {
            echo '❌ Une étape a échoué — vérifiez les logs et les rapports générés.'
        }
    }
}
