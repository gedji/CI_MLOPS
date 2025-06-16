import dagshub
dagshub.init(repo_owner='gedji', repo_name='CI_MLOPS', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)