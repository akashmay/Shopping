pipeline {
    agent any  // This defines where the pipeline will run
    // tools {
    //     git 'Windows-git'  // If you are using a custom Git installation
    // }

    environment {
        PYTHON_VENV = 'C:\\jenkins\\python_venv'  // Specify the path for your Python virtual environment
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout code from Git repository
                    checkout scm
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Install Python dependencies from requirements.txt
                    bat '''
                        REM Check if Python is available in PATH
                        where python >nul 2>nul
                        IF %ERRORLEVEL% NEQ 0 (
                            echo Python not found in PATH. Please install Python and add it to PATH.
                            exit /b 1
                        )

                        REM Create a virtual environment (if not exists)
                        IF NOT EXIST "%PYTHON_VENV%" (
                            python -m venv %PYTHON_VENV%
                        )

                        REM Activate the virtual environment
                        set VIRTUAL_ENV=%PYTHON_VENV%
                        set PATH=%VIRTUAL_ENV%\\Scripts;%PATH%

                        REM Upgrade pip and install dependencies
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run pytest automation using CMD (Batch)
                    bat '''
                        REM Ensure the virtual environment is activated
                        set VIRTUAL_ENV=%PYTHON_VENV%
                        set PATH=%VIRTUAL_ENV%\\Scripts;%PATH%

                        REM Run pytest automation
                        pytest test_cases\\pipeline {
    agent any  // This defines where the pipeline will run
    // tools {
    //     git 'Windows-git'  // If you are using a custom Git installation
    // }

    environment {
        PYTHON_VENV = 'C:\\jenkins\\python_venv'  // Specify the path for your Python virtual environment
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout code from Git repository
                    checkout scm
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Install Python dependencies from requirements.txt
                    bat '''
                        REM Check if Python is available in PATH
                        where python >nul 2>nul
                        IF %ERRORLEVEL% NEQ 0 (
                            echo Python not found in PATH. Please install Python and add it to PATH.
                            exit /b 1
                        )

                        REM Create a virtual environment (if not exists)
                        IF NOT EXIST "%PYTHON_VENV%" (
                            python -m venv %PYTHON_VENV%
                        )

                        REM Activate the virtual environment
                        set VIRTUAL_ENV=%PYTHON_VENV%
                        set PATH=%VIRTUAL_ENV%\\Scripts;%PATH%

                        REM Upgrade pip and install dependencies
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run pytest automation using CMD (Batch)
                    bat '''
                        REM Ensure the virtual environment is activated
                        set VIRTUAL_ENV=%PYTHON_VENV%
                        set PATH=%VIRTUAL_ENV%\\Scripts;%PATH%

                        REM Run pytest automation
                        pytest test_cases\\UI_tests\\Test_Account_Login.py -v -s --browser=chrome
                    '''
                }
            }
        }
    }
}\\update_headline.py -v -s --browser=chrome
                    '''
                }
            }
        }
    }
}
