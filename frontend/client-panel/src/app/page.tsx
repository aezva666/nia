import { NIAChat } from '@/components/nia/chat';

export default function Home() {
  return (
    <main className="min-h-screen p-4">
      <div className="container mx-auto">
        <h1 className="text-3xl font-bold text-center mb-8">Bienvenido a NIA</h1>
        <NIAChat />
      </div>
    </main>
  );
} 