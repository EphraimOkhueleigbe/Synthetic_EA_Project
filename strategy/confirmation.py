def add_confirmation(d1, m30):


    signals = []


    waiting_for_confirmation = False

    active_direction = 0

    retrace_time = None



    for i in range(len(d1)):


        current_time = d1.index[i]


        signal = "NONE"



        # Detect NEW retracement event

        if d1["Retracement"].iloc[i]:


            if not waiting_for_confirmation:


                waiting_for_confirmation = True

                active_direction = d1["Trend"].iloc[i]

                retrace_time = current_time



        # Scan only NEW M30 candles after retracement

        if waiting_for_confirmation:


            valid_m30 = m30[
                m30.index > retrace_time
            ]



            for j in range(1, len(valid_m30)):


                prev_fast = valid_m30["EMA_9"].iloc[j-1]

                prev_slow = valid_m30["EMA_18"].iloc[j-1]


                curr_fast = valid_m30["EMA_9"].iloc[j]

                curr_slow = valid_m30["EMA_18"].iloc[j]



                # BUY

                if active_direction == 1:


                    if (
                        prev_fast <= prev_slow
                        and
                        curr_fast > curr_slow
                    ):


                        signal = "BUY"

                        waiting_for_confirmation = False

                        break



                # SELL

                if active_direction == -1:


                    if (
                        prev_fast >= prev_slow
                        and
                        curr_fast < curr_slow
                    ):


                        signal = "SELL"

                        waiting_for_confirmation = False

                        break



        signals.append(signal)



    d1["Signal"] = signals


    return d1