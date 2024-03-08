from torch.optim.lr_scheduler import LambdaLR


def linear_schedule_with_warmup(optimizer, 
                                num_warmup_steps, 
                                num_training_steps, 
                                last_epoch=-1):
    """Linear warmup and then linear decay.
    """
    
    def lr_lambda(current_step):
        if current_step < num_warmup_steps:
            return float(current_step) / float(max(1, num_warmup_steps))
        return max(0.0, float(num_training_steps - current_step) / float(max(1, num_training_steps - num_warmup_steps)))

    return LambdaLR(optimizer=optimizer, lr_lambda=lr_lambda, last_epoch=last_epoch)