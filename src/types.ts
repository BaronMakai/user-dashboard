interface User {
  id: number;
  name: string;
  email: string;
  password: string;
  role: string;
  createdAt: Date;
  updatedAt: Date;
}

interface UserResponse {
  id: number;
  name: string;
  email: string;
  password: string;
  role: string;
  createdAt: Date;
  updatedAt: Date;
}

interface UserCreate {
  id: number;
  name: string;
  email: string;
  password: string;
  role: string;
}

interface UserUpdate {
  id: number;
  name: string;
  email: string;
  password: string;
  role: string;
  updatedAt: Date;
}

interface UserDelete {
  id: number;
}