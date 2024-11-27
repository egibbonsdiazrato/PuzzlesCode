import numpy as np
import plotly.graph_objects as go

if __name__ == '__main__':
    # Flags for plotting
    plot_2D = True
    plot_3D = True

    if plot_2D:
        # Parameters for a square of side 1 w/ bottom left corner on (0,0)
        x_square = np.array([0, 1, 1, 0, 0])
        y_square = np.array([0, 0, 1, 1, 0])
        lims = [0.5, 1]

        # Plotting
        fig = go.Figure()  # Figure creation

        # Plot squares where the minimum is greater than either of the limits
        for lim in lims:
            # Resize and shift the square
            x = lim*np.ones_like(x_square) + (3 - lim)*x_square
            y = lim*np.ones_like(y_square) + (3 - lim)*y_square
            # Area where the minimum of x_i and x_j is greater than the lim value
            fig.add_trace(go.Scatter(x=x, y=y, fill='toself', name=fr'$min(x_1, x_2) \geq {lim}$'))

        # L-shaped area
        fig.add_trace(go.Scatter(x=[0.5, 3, 3, 1, 1, 0.5, 0.5],
                                 y=[0.5, 0.5, 1, 1, 3, 3, 0.5],
                                 fill='toself',
                                 name=r'$0.5 \leq min(x_1, x_2) \leq 1$',
                                 ))

        # Update the rest of the figure
        fig.update_layout(title='2D Simplification',
                          xaxis={'title': {'text': r'$x_1$', 'font': {'size': 18}},
                                 'range': [-0.25, 3.25],
                                 },
                          yaxis={'title': {'text': r'$x_2$', 'font': {'size': 18}},
                                 'range': [-0.25, 3.25],
                                 },
                          width=1200, height=1200)

        fig.show()

    if plot_3D:
        bounds = [0, 3]
        N_samples = int(1e6)

        x = np.random.uniform(bounds[0], bounds[1], N_samples)
        y = np.random.uniform(bounds[0], bounds[1], N_samples)
        z = np.random.uniform(bounds[0], bounds[1], N_samples)

        inds_satisfy_cond = [(min(x[i], y[i], z[i]) >= 0.5) & (min(x[i], y[i], z[i]) <= 1.0) for i in range(0, N_samples)]

        # Plotting
        fig = go.Figure(data=[go.Scatter3d(x=x[inds_satisfy_cond],
                                           y=y[inds_satisfy_cond],
                                           z=z[inds_satisfy_cond],
                                           mode='markers',
                                           marker=dict(size=2, color=z[inds_satisfy_cond], colorscale='Viridis'))])

        # Update the rest of the figure
        fig.update_layout(title='3D Exploration',
                          scene={'xaxis_title': {'text': 'x_1', 'font': {'size': 18}},
                                 'yaxis_title': {'text': 'x_2', 'font': {'size': 18}},
                                 'zaxis_title': {'text': 'x_3', 'font': {'size': 18}},
                                 'xaxis': {'range': [-0.25, 3.25]}, 'yaxis': {'range': [-0.25, 3.25]},
                                 'zaxis': {'range': [-0.25, 3.25]}},
                          width=1200, height=1200)

        fig.show()

        print(f'The approximate volume by MC is: {sum(inds_satisfy_cond)/N_samples}')
        print(f'This may be compared to the analytical solution which is: {61/216}')
