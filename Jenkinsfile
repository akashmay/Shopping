pipeline {
    agent { label 'my_laptop' }

    // Use the globally configured Git tool for the Unix node.
    tools {
        git 'Git'
    }

    parameters {
        choice(name: 'TEST_SUITE', choices: ['UI', 'API', 'PDF'], description: 'Select test suite to run')
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Using SSH credentials with id '2' for the Unix machine.
                sshagent(credentials: ['2']) {
                    // Check out the 'main' branch from GitHub.
                    git branch: 'main', url: 'git@github.com:akashmay/ShoppingCart.git'
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Ensure pip is installed and up-to-date
                sh 'python3 -m ensurepip --upgrade'  // For Unix systems, use 'python3'
                sh 'python3 -m pip install
