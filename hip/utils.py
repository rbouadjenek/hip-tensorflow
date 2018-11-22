import numpy as np
import matplotlib.pyplot as plt

def plot_predictions(y_truth, y_predictions, xs=None, train_test_split_point=0.8, legend=True):
        """
            Plot the current predictions from the fitted model 
        """
        num_of_series = len(y_truth)
        data_length = len(y_truth[0])
        data_test_split_point = (int)(data_length * train_test_split_point)

        srows = (int)(np.ceil(np.sqrt(num_of_series)))

        fig, axes = plt.subplots(srows, srows, sharex='all')
        for i in range(num_of_series):
            row = (int)(i / srows)
            col = (int)(i % srows)

            truth = y_truth[i]
            pred = y_predictions[i]

            if num_of_series == 1:
                ax = plt
            else:
                ax = axes[row, col]

            ax.axvline(data_test_split_point, color='k')
            ax.plot(np.arange(data_length), truth, 'k--', label='Observed #views')

            if xs is not None:
                x = xs[i]
                
                colors = iter(plt.cm.rainbow(np.linspace(0, 1, len(x))))
                for index, exo_source in enumerate(x):
                    c = next(colors)
                    ax.plot(np.arange(data_length), exo_source, c=c, alpha=0.3)

            # plot predictions on training data with a different alpha to make the plot more clear            
            ax.plot(
                        np.arange(data_test_split_point+1),
                        pred[:data_test_split_point+1], 
                        'b-',
                        alpha=0.5,
                        label='Model Fit'
                    )
            ax.plot(
                        np.arange(data_test_split_point, data_length),
                        pred[data_test_split_point:], 
                        'b-',
                        alpha=1,
                        label='Model Predictions'
                    )

        return axes

def get_test_rmse(truth, predictions, train_test_split=0.8):
        loss = 0
        split_point = (int)(train_test_split * len(truth[0])) + 1

        for i in range(len(predictions)):
            y_truth = truth[i][split_point:]
            y_pred = predictions[i][split_point:]

            loss += np.sqrt(np.sum(y_pred - y_truth) ** 2) / len(y_truth)
    
        return loss


class TimeSeriesScaler():
    def transform_x(self, xs):
        scaled_xs = []
        for x_series in xs:
            scaled_x_series = []
            for x in x_series:
                x_min = np.min(x)
                x_max = np.max(x)
                scaled_x = (x - x_min) / (x_max - x_min)

                scaled_x_series.append(scaled_x)
            scaled_xs.append(scaled_x_series)

        return scaled_xs
    
    def transform_y(self, ys):
        self.y_mins = []
        self.y_maxs = []

        scaled_ys = []
        for y in ys:
            y_min = np.min(y)
            y_max = np.max(y)

            self.y_mins.append(y_min)
            self.y_maxs.append(y_max)
            scaled_y = (y - y_min) / (y_max - y_min)

            scaled_ys.append(scaled_y)

        return scaled_ys

    def invert_transform_y(self, scaled_ys):
        rescaled_ys = []
        for index, scaled_y in enumerate(scaled_ys):
            rescaled_y = (
                            scaled_y * (self.y_maxs[index] - self.y_mins[index]) +
                            self.y_mins[index]
                        )  

            rescaled_ys.append(rescaled_y)

        return rescaled_ys