import express from 'express';
import { PrismaClient } from '@prisma/client';

const app = express();
const prisma = new PrismaClient();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.json({ message: 'API en ejecución' });
});

app.get('/api/productos', async (req, res) => {
  try {
    const productos = await prisma.product.findMany();
    res.json(productos);
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener productos', details: error.message });
  }
});

app.post('/api/productos', async (req, res) => {
  try {
    const { nombre, precio, descripcion } = req.body;
    const nuevoProducto = await prisma.product.create({
      data: {
        nombre,
        precio: parseFloat(precio),
        descripcion
      }
    });
    res.status(201).json(nuevoProducto);
  } catch (error) {
    res.status(500).json({ error: 'Error al crear producto', details: error.message });
  }
});

app.delete('/api/productos/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const productoEliminado = await prisma.product.delete({
      where: { id: parseInt(id) }
    });
    res.json({ message: 'Producto eliminado correctamente', producto: productoEliminado });
  } catch (error) {
    res.status(500).json({ error: 'Error al eliminar producto', details: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Servidor corriendo en puerto ${PORT}`);
});