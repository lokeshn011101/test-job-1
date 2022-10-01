# Replace `YOUR_SECRET_FQN`, `YOUR_WORKSPACE_FQN`
# with the actual values.
import logging

from servicefoundry import (
    Build,
    Job,
    PythonBuild,
)

logging.basicConfig(level=logging.INFO)

# NOTE: Here we are defining the image build specification.
# servicefoundry uses this specification to automatically create
# a Dockerfile and build an image,
image = Build(
    build_spec=PythonBuild(
        command="python train.py",
        requirements_path="train_requirements.txt",
    )
)
env = {
    # NOTE:- We will automatically map the secret value to the environment variable.
    "MLF_API_KEY": "tfy-secret://user-truefoundry:test-lokesh:api_key",
}


job = Job(
    name="training-job",
    image=image,
    env=env,
)
job.deploy(workspace_fqn="local:lokesh-test")