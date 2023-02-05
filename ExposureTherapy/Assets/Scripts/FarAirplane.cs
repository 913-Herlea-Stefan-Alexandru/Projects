using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FarAirplane : MonoBehaviour
{
    public float flySpeed = 40f;
    public float ascendSpeed = 20f;

    public float distanceLimit = 500f;

    // Start is called before the first frame update
    void Start()
    {
        GetComponent<AudioSource>().Play();
    }

    // Update is called once per frame
    void Update()
    {
        float distance = flySpeed * Time.deltaTime;
        distanceLimit -= distance;
        transform.Translate(0f, ascendSpeed * Time.deltaTime, -distance);
        if (distanceLimit <= 0)
        {
            Destroy(gameObject);
        }
    }
}
