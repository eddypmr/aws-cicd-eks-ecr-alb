# AWS CI/CD – EKS · ECR · ALB (GitHub Actions + OIDC)

Proyecto DevOps que implementa una **API contenerizada** desplegada en **Amazon EKS**, expuesta públicamente mediante **AWS Application Load Balancer (ALB)** y automatizada con **CI/CD desde GitHub Actions usando OIDC** (sin credenciales estáticas).

---

## 🎯 Objetivo del proyecto

Diseñar y validar un flujo **end-to-end DevOps** que cubra:

- Contenerización de una API
- Publicación de imágenes en Amazon ECR
- Despliegue en Kubernetes (EKS)
- Exposición pública mediante ALB Ingress
- Seguridad basada en IAM Roles + OIDC
- Infraestructura reproducible y sin costes persistentes

---

## 🏗️ Arquitectura

- **API**: FastAPI (Python)
- **Contenedor**: Docker
- **Registry**: Amazon ECR
- **Orquestador**: Amazon EKS
- **Exposición pública**: AWS Load Balancer Controller (ALB Ingress)
- **CI/CD**: GitHub Actions
- **Autenticación CI/CD → AWS**: OIDC (sin access keys)
- **Persistencia**: DynamoDB (acceso mediante IRSA)

Flujo:
```
GitHub → GitHub Actions → OIDC → IAM Role → Docker Build → ECR → kubectl apply → EKS → ALB → Internet
```

---

## 📂 Estructura del repositorio

```
.
├── app/ # Código de la API (FastAPI)
│ ├── main.py
│ ├── db.py
│ └── models.py
│
├── docker/
│ └── Dockerfile
│
├── k8s/ # Manifiestos Kubernetes
│ ├── namespace.yaml
│ ├── deployment.yaml
│ ├── service.yaml
│ ├── ingress.yaml
│ ├── configmap.yaml
│ └── serviceaccount.yaml
│
├── scripts/ # Scripts de validación manual
│ ├── 00_env.sh
| ├ ----
│ └── 99_*.sh
│
└── .github/workflows/ # Pipelines CI/CD
            └── deploy.yml
```


---

## 🚀 API – Endpoints disponibles

Una vez desplegada y expuesta por ALB:

- `GET /health` → Healthcheck
- `POST /services` → Registrar servicios a monitorizar
- `GET /services` → Listado de servicios
- `GET /status` → Estado actual de los servicios
- `GET /status/{service_id}/latest`
- `GET /status/{service_id}/history`

---

## 🔐 Seguridad

- ❌ **Sin AWS Access Keys**
- ✅ Autenticación mediante **OIDC**
- ✅ Roles IAM con permisos mínimos
- ✅ Acceso a DynamoDB usando **IRSA (IAM Roles for Service Accounts)**

---

## 🧪 Validación y pruebas

- El despliegue se validó inicialmente mediante **scripts manuales**
- Una vez validado, se automatizó mediante **GitHub Actions**
- El cluster EKS y los recursos AWS se destruyen tras las pruebas para evitar costes

---

## 💸 Gestión de costes

- Uso de `t3.micro`
- Infraestructura efímera
- Cluster destruido tras validación
- Proyecto pensado para **free tier / bajo coste**

---

## 📌 Estado del proyecto

✅ CI/CD funcional  
✅ API accesible públicamente  
✅ Infraestructura validada  
🧹 Recursos AWS eliminados tras pruebas  

---

## 🧠 Aprendizajes clave

- Diseño de pipelines CI/CD seguros con OIDC
- Uso real de EKS + ALB Controller
- Debugging de Kubernetes (ConfigMaps, Probes, IRSA, Ingress)
- Buenas prácticas DevOps orientadas a producción

---

## 👤 Autor

Eddy Patrik Morocho Realpe
Proyecto desarrollado como parte de un **portfolio DevOps / Cloud Engineer**.
