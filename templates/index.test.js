import { render, screen, fireEvent } from '@testing-library/react';
import App from '../main'; // Assuming your main component is App

test('adds Pokémon to squad and enables Battle button', () => {
    render(<App />);
    
    const pikachuButton = screen.getByText('Add to Squad', { selector: 'button' });
    fireEvent.click(pikachuButton);
    fireEvent.click(pikachuButton); // Try adding Pikachu twice

    const squadItems = screen.getAllByText('Pikachu');
    expect(squadItems.length).toBe(1); // Pikachu should appear only once

    const battleButton = screen.getByText('Battle');
    expect(battleButton).toBeDisabled(); // Battle button should be disabled

    // Add another Pokémon to enable Battle button
    const bulbasaurButton = screen.getByText('Add to Squad', { selector: 'button' });
    fireEvent.click(bulbasaurButton);

    expect(battleButton).toBeEnabled(); // Battle button should be enabled
});
