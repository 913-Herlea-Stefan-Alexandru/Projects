package model.adt;

import java.util.List;

public class SemaphoreDTO {
    private int address;
    private int permits;
    private String states;

    public SemaphoreDTO(int address, int permits, String states) {
        this.address = address;
        this.permits = permits;
        this.states = states;
    }

    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }

    public int getPermits() {
        return permits;
    }

    public void setPermits(int permits) {
        this.permits = permits;
    }

    public String getStates() {
        return states;
    }

    public void setStates(String states) {
        this.states = states;
    }

    @Override
    public String toString() {
        return "" + address + " | " + permits + " | " + states.toString();
    }
}
