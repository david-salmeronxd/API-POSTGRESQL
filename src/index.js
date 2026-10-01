import express from 'express';
import { PrismaClient } from '@prisma/client';

const app = express();
const prisma = new PrismaClient();

app.use(express.json());

app.get('/productos', async (req, res) => {
  const productos = await prisma.producto.findMany();
  res.json(productos);
});


app.post('/productos', async (req, res) => {
  const { nombre, precio } = req.body;
  const nuevoProducto = await prisma.producto.create({
    data: { nombre, precio: parseFloat(precio) }
  });
  res.status(201).json(nuevoProducto);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});