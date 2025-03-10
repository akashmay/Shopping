pipeline {
    agent { label 'my_laptop' }

    // Use the globally configured Git tool for the Windows node.
    tools {
        git 'GitForWindows'
    }

    parameters {
        choice(name: 'TEST_SUITE', choices: ['UI', 'API', 'PDF'], description: 'Select test suite to run')
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Using SSH credentials with id '2' for the Windows machine.
                sshagent(credentials: ['2']) {
                    // Check out the 'main' branch from GitHub.
                    git branch: 'main', url: 'git@github.com:akashmay/ShoppingCart.git'
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m ensurepip'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Selected Tests') {
            steps {
                bat 'if not exist reports mkdir reports'  // Ensure reports directory exists
                script {
                    def testCommand = ""
                    if (params.TEST_SUITE == 'UI') {
                        testCommand = 'pytest test_cases/UI_tests --html=reports/ui_test_report.html --self-contained-html'
                    } else if (params.TEST_SUITE == 'API') {
                        testCommand = 'pytest test_cases/API_tests --html=reports/api_test_report.html --self-contained-html'
                    } else if (params.TEST_SUITE == 'PDF') {
                        testCommand = 'pytest test_cases/PDF_tests --html=reports/pdf_test_report.html --self-contained-html'
                    }
                    bat testCommand
                }
            }
        }

        stage('Publish Reports') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: '*.html',
                    reportName: 'Test Reports'
                ])
            }
        }
    }
}
