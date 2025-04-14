import express from 'express';
import dotenv from 'dotenv';
import cors from 'cors';
import { connectDB, disconnectDB } from './config/db';

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

connectDB();

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

dotenv.config();

