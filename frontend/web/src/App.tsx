
import { RouterProvider } from 'react-router-dom';
import { router } from '@core/routing/AppRouter';

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
