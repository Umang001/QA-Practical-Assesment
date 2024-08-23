# Problem Statement 1

## Kubernetes Deployment

### Prerequisites

Ensure that you have `Docker`,  `Kubectl`,  `Minikube` installed and running on your machine. You can verify the installations by running the following commands:

- **Docker:**  
  ```bash
  docker version 
  ```

- **Kubectl:**  
  ```bash
  kubectl version
  ```

- **Minikube:**  
  ```bash
  minikube version
  ```
 
If they are not installed, you can follow the official installation guides:

- [Docker Installation Guide](https://docs.docker.com/engine/install/)
- [Kubectl Installation Guide](https://kubernetes.io/docs/tasks/tools/)
- [Minikube Installation Guide](https://minikube.sigs.k8s.io/docs/start/)

#### Step 1: Clonning the repo
- Clone the repo via git clone https://github.com/Vengatesh-m/qa-test.git

#### Step 2: Deploying the Service 
- Navigate to Deployment folder and run below command. This command will deploy the service.
  ```bash
  kubectl apply -f .
  ```

## Verification

#### Step 1: Verify the pod are running 
- Run the below command to verify all the pods are running 
  ```bash
  kubectl get pod
  ```

#### Step 2: Verify the services are created properly 
- Run the below command to verify all the pods are running 
  ```bash
  kubectl get services
  ```

#### Step 3: Verify the deployment is proper
- Run the below command to verify all the pods are running 
  ```bash
  kubectl get deployments
  ```

#### Step 4: Attach the backend service to frontend service
- Run the below command from frontend pod to attach the backend service
  ```bash
  kubectl exec -it <frontend-pod> -- bash
  nc -zv backend.service.default.service.cluster.local 3000
  ```

#### Step 5: Forward the port to access the frontend
- Run the below command to forward the frontend port 
  ```bash
  kubectl port-forward svc/frontend-service 8080:80
  ```

#### Step 6: Access the frontend url
- Navigate to any browser and try accessing the url:
  ```bash
  http://127.0.0.1:8080
  ```

## Automated Testing

To run the script, first set up a virtual environment:
```bash
❯ python -m venv venv
❯ . venv/bin/activate
❯ pip install -r requirements.txt
❯ python test_integrate.py
```
