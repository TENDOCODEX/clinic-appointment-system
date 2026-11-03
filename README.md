# Clinic Appointment Management System

## 1. Project Description

This project is a Clinic Appointment Management System developed using Python.

It represents patients, clinic staff and appointments using Object-Oriented Programming principles.

## 2. Class Diagram

```mermaid
classDiagram
    class Person {
        <<abstract>>
        -name
        -id
        +role()*
    }

    class Patient {
        +role()
    }

    class Staff {
        <<abstract>>
        +fee()*
    }

    class Doctor {
        +role()
        +fee()
    }

    class Nurse {
        +role()
        +fee()
    }

    class Pharmacist {
        +role()
        +fee()
    }

    class Appointment {
        -appointment_id
        -patient
        -staff
        -start_hour
        -duration
    }

    class Clinic {
        -name
        -appointments
        +add_appointment()
    }

    Person <|-- Patient
    Person <|-- Staff
    Staff <|-- Doctor
    Staff <|-- Nurse
    Staff <|-- Pharmacist
    Appointment --> Patient : books
    Appointment --> Staff : assigned to
    Clinic o-- Appointment : manages
```
