# start time of our data
start_time = '2009-01-01'

#last date of data including labels and outcomes that we have
end_time = '2016-01-01'

#how far out do we want to predict (let's say in months for now)
prediction_windows = [6, 12]

#how often is this prediction being made? every day? every month? once a year?
update_window = 12

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

start_time_date = datetime.strptime(start_time, '%Y-%m-%d')
end_time_date = datetime.strptime(end_time, '%Y-%m-%d')

for prediction_window in prediction_windows:
    # End testing at end of available time period
    test_end_time = end_time_date
    # while test_end_time is greater than or equal to start_time_date + twice the length of the prediction window (i.e. the length of a training and testing set)
    while (test_end_time >= start_time_date + 2 * relativedelta(months=+prediction_window)):
        # set start time of test x months prior to test end time, where x is the length of the prediction window
        test_start_time = test_end_time - relativedelta(months=+prediction_window)
        # set train end time equal to test start -1 day
        train_end_time = test_start_time  - relativedelta(days=+1) # minus 1 day
        # Set training start time x months prior to train end time, where x is the length of the prediction window
        train_start_time = train_end_time - relativedelta(months=+prediction_window)
        # while start time of the training set is after the start time of the whole data set
        while (train_start_time >= start_time_date):
            # print the  starting/eding times of the train and test sets
            print train_start_time,train_end_time,test_start_time,test_end_time, prediction_window
            
            train_start_time -= relativedelta(months=+prediction_window)
            # call function to get data
            train_set, test_set = extract_train_test_sets (train_start_time, train_end_time, test_start_time, test_end_time)
            # fit on train data
            # predict on test data
        test_end_time -= relativedelta(months=+update_window)