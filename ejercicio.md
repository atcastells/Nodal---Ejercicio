Nodal - Prueba Técnica


Rol: Lead Full Stack Developer / System Architect 
Modalidad: Open-Ended Problem 
Tiempo estimado: 4 - 6 horas 
Stack: Python (El resto lo decides tú)
1. El Problema de Negocio
En Nodal, estamos construyendo un sistema de "Diseño Generativo" donde el estado de un proyecto no es estático, sino reactivo. Un cambio en una fase temprana (ej: Briefing) invalida y desencadena procesos en fases posteriores (Research, Ingeniería) que pueden tardar segundos o minutos en resolverse mediante IA.
Necesitamos un Engine de Backend capaz de gestionar este caos de forma robusta.
2. Tu Misión
Diseña e implementa un MVP del "Núcleo Reactivo" de Nodal.
Requerimientos Funcionales (El "Qué")
El sistema debe manejar una entidad Project que contiene un estado complejo (Brief, Research, DFM, Créditos).
Mutación Reactiva: Cuando el usuario modifica el brief, el sistema debe evaluar la magnitud del cambio.
Si es un cambio menor: Solo actualiza el dato.
Si es un cambio mayor: Debe invalidar los estados dependientes (Research/DFM), descontar créditos de forma segura y re-ejecutar esos procesos automáticamente.
Simulación de Latencia: Los procesos de Research y DFM no son inmediatos. Simula que son llamadas a APIs externas (LLMs) que tardan varios segundos.
Observabilidad: El frontend debe ser capaz de saber en qué estado está cada parte del proyecto en todo momento.

Requerimientos No Funcionales (El "Cómo" - Aquí es donde te evaluamos)
Consistencia de Datos: El sistema manejará alta concurrencia. Evita race conditions (ej: doble gasto de créditos).
Mantenibilidad: El sistema va a crecer. Hoy usamos Postgres, mañana quizás no. Hoy es FastAPI, mañana quizás no. Diseña una arquitectura que soporte cambios.
Testing en la Era de la IA: El sistema produce salidas no deterministas (texto generado por IA). ¿Cómo aseguras la calidad automática de este código?
3. Entregables
No queremos solo código que "funcione". Queremos código que "escale".
Repositorio Git: Con todo lo necesario para arrancar el entorno (Docker es un plus).
README - La Defensa de tu Diseño:
Este es el punto más importante. Explica por qué elegiste esa arquitectura.
Justifica tu estrategia de concurrencia.
Explica tu enfoque para testear componentes de IA.

